import { create } from "zustand";
const initialState = {
  bears: 0,
};
export const useMainStore = create((set) => ({
  // Initial Values
  ...initialState,
  increasePopulation: () => set((state) => ({ bears: state.bears + 1 })),
  removeAllBears: () => set({ bears: 0 }),
}));
if (process.env.NODE_ENV === "development") {
  mountStoreDevtool("Main Store", useMainStore);
}
