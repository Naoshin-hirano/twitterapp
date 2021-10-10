import { shallowMount } from "@vue/test-utils";
import { mount } from "@vue/test-utils";
import List from "@/views/Home/List.vue";
import "isomorphic-fetch"

describe("List.vue", () => {
  it("renders props.msg when passed", () => {
    const wrapper = shallowMount(List);
    expect(wrapper.text()).toContain("ホーム");
  });

  it("should add new list", async () => {
      const wrapper = mount(List);
      
      expect(wrapper.findAll('[data-test="list"]')).toHaveLength(1);

      await wrapper.get('[data-test="content"]').setValue('New Post');
      await wrapper.get('[data-test="form"]').trigger('submit')

      expect(wrapper.find('textarea').element.value).toBe('New Post')

      expect(wrapper.findAll('[data-test="list"]')).toHaveLength(2);
  });
});
