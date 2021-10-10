import { shallowMount } from "@vue/test-utils";
import { mount } from "@vue/test-utils";
import List from "@/views/Home/List.vue";
import "isomorphic-fetch"

describe("List.vue", () => {
    let wrapper;
    
    beforeEach(() => {
        wrapper = mount(List); 
    });

  it("renders props.msg when passed", () => {
    wrapper = shallowMount(List);
    expect(wrapper.text()).toContain("ホーム");
  });

  it("should add new list", async () => {
      wrapper = mount(List);
      
      expect(wrapper.findAll('[data-test="list"]')).toHaveLength(1);

      await wrapper.get('[data-test="content"]').setValue('New Post');
      await wrapper.get('[data-test="form"]').trigger('submit')

      expect(wrapper.find('textarea').element.value).toBe('New Post')

      expect(wrapper.findAll('[data-test="list"]')).toHaveLength(2);
  });
});
